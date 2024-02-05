import redis


class Leaderboard:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
        self.leaderboard_key = 'game_leaderboard'
        self.users_key = 'users'

    def register_user(self, username, password):
        if self.redis_client.hexists(self.users_key, username):
            print("User exists.")
            return False
        self.redis_client.hset(self.users_key, username, password)
        return True

    def login(self, username, password):
        stored_password = self.redis_client.hget('users', username)
        if stored_password == password:
            print(f"Hello, {username}.")
            self.current_user = username
            return True
        else:
            print("Wrong login or password.")
            return False

    def add_result(self, score):
        if hasattr(self, 'current_user'):
            self.redis_client.zadd(self.leaderboard_key, {self.current_user: score})
            print(f"Added {self.current_user}: {score}")

    def remove_result(self):
        if hasattr(self, 'current_user'):
            self.redis_client.zrem(self.leaderboard_key, self.current_user)
            print(f"Removed {self.current_user}")

    def update_result(self, score):
        if hasattr(self, 'current_user'):
            self.redis_client.zadd(self.leaderboard_key, {self.current_user: score})
            print(f"Updated {self.current_user}: {score}")

    def clear_leaderboard(self):
        self.redis_client.delete(self.leaderboard_key)
        print("Cleared")

    def search_result(self, username):
        score = self.redis_client.zscore(self.leaderboard_key, username)
        if score is not None:
            print(f"Result {username}: {score}")
        else:
            print(f"Result for {username} is not found.")

    def view_leaderboard(self):
        leaderboard = self.redis_client.zrevrange(self.leaderboard_key, 0, 9, withscores=True)
        if leaderboard:
            print("TOP 10:")
            for rank, (username, score) in enumerate(leaderboard, start=1):
                print(f"{rank}. {username}: {score}")
        else:
            print("Empty.")


leaderboard_app = Leaderboard()
leaderboard_app.register_user("user1", "password")
if leaderboard_app.login("user1", "password"):
    leaderboard_app.add_result(100)

    leaderboard_app.view_leaderboard()

    leaderboard_app.update_result(150)

    leaderboard_app.search_result("user1")

    leaderboard_app.remove_result()

    leaderboard_app.view_leaderboard()

    leaderboard_app.clear_leaderboard()
    leaderboard_app.view_leaderboard()
