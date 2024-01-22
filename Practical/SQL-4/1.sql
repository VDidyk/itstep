--1. Виведіть повні імена лікарів та їх спеціалізації.--
select concat(doctors.name, ' ' ,doctors.surname), string_agg(specializations.name,', ') from doctors
left join doctorsspecializations on doctorsspecializations.doctor_id = doctors.id
left join specializations on specializations.id=doctorsspecializations.specialization_id
group by doctors.id

--2. Виведіть прізвища та зарплати (сума ставки та надбавки) лікарів, які не перебувають у відпустці.
select concat(doctors.name, ' ' ,doctors.surname) from doctors
where not exists (select * from vacations where doctor_id=doctors.id and current_date between start_date and end_date)

--3. Виведіть назви палат, які знаходяться у відділенні «Intensive Treatment».--
select wards.name from wards
left join departments on departments.id = wards.department_id
where departments.name = 'Intensive Treatment';

--4. Виведіть назви відділень без повторень, які спонсоруються компанією «Umbrella Corporation»--
select departments.name from departments
left join donations on donations.department_id = departments.id
left join sponsors on donations.sponsor_id = sponsors.id
where sponsors.name = 'Umbrella Corporation';

--5. Виведіть усі пожертвування за останній місяць у вигляді: відділення, спонсор, сума пожертвування, дата пожертвування--
select departments.name,sponsors.name,donations.amount, donations.date from donations
left join departments on donations.department_id = departments.id
left join sponsors on donations.sponsor_id = sponsors.id
WHERE EXTRACT(MONTH FROM donations.date) = EXTRACT(MONTH FROM CURRENT_DATE)
AND EXTRACT(YEAR FROM donations.date) = EXTRACT(YEAR FROM CURRENT_DATE);

--6. Виведіть прізвища лікарів із зазначенням відділень, в яких вони проводять обстеження. Враховуйте обстеження, які проводяться лише у будні дні.--
select concat(doctors.name,' ',doctors.surname), string_agg(examinations.name, ', ') from doctors
left join doctors_examinations on doctors_examinations.doctor_id = doctors.id
left join examinations on doctors_examinations.examination_id = examinations.id and examinations.dayofweek between 0 and 5
group by doctors.id

--7. Виведіть назви відділень, які отримували пожертву-вання у розмірі понад 100000, із зазначенням їх лікарів.--
select departments.name, string_agg(doctors.name,', ') from departments
left join doctors_departments on doctors_departments.department_id = departments.id
left join doctors on doctors_departments.doctor_id = doctors.id
JOIN (
    SELECT department_id, SUM(amount) as total_amount
    FROM donations
    GROUP BY department_id
) as donation_sums ON departments.id = donation_sums.department_id
WHERE donation_sums.total_amount > 10000
group by departments.id

--8. Виведіть назви відділень, в яких лікарі не отримують надбавки.--
select departments.name from departments
where exists (
	select * from doctors
	left join doctors_departments on doctors_departments.doctor_id = doctors.id
	where doctors_departments.department_id = departments.id and (doctors.premium = 0 or doctors.premium is null)
)

--Не хотів вже створювати звʼязок з хворобами--
--9. Виведіть назви відділень і назви захворювань, обстеження з яких вони проводили за останні півроку--
select departments.name, string_agg(examinations.name,', ') from departments
join doctors_departments on doctors_departments.department_id = departments.id
join doctors_examinations on doctors_examinations.doctor_id = doctors_departments.doctor_id
join examinations on examinations.id=doctors_examinations.examination_id
join examinationdates on examinations.id=examinationdates.examinationid
WHERE examinationdates.examinationdate >= current_date - interval '6 months'
group by departments.id