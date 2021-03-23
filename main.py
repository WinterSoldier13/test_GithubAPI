import requests


class Solution:

    def getFollowers(self, username):
        followers_URL = 'https://api.github.com/users/'+username+'/followers'
        followers_req = requests.get(url=followers_URL)
        followers_data = followers_req.json()

        hashmap = {}

        for follower in followers_data:
            hashmap[follower['login']] = follower['html_url']

        # for key in hashmap.keys():
        #     print(key, " -> ", hashmap[key])

        return hashmap

    def getFollowing(self, username):
        following_URL = 'https://api.github.com/users/'+username+'/following'
        following_req = requests.get(url=following_URL)
        following_data = following_req.json()

        hashmap = {}

        for following in following_data:
            hashmap[following['login']] = following['html_url']

        # for key in hashmap.keys():
        #     print(key, " -> ", hashmap[key])

        return hashmap

    def getDifference(self, username):
        followers_hashmap = self.getFollowers(username)
        following_hashmap = self.getFollowing(username)

        differenceHashmap = {}

        for following in following_hashmap.keys():
            if(not following in followers_hashmap.keys()):
                differenceHashmap[following] = following_hashmap[following]
        
        for key in differenceHashmap.keys():
            print(key, " -> ", differenceHashmap[key])
        
        return differenceHashmap
    
    def getPeopleWhomYouDontFollowBack(self, username):
        following_hashmap = self.getFollowers(username)
        followers_hashmap = self.getFollowing(username)

        differenceHashmap = {}

        for following in following_hashmap.keys():
            if(not following in followers_hashmap.keys()):
                differenceHashmap[following] = following_hashmap[following]
        
        for key in differenceHashmap.keys():
            print(key, " -> ", differenceHashmap[key])

        return differenceHashmap


ob = Solution()

ob.getDifference('WinterSoldier13')
