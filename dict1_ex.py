name,age,fav_movie,fav_songs,hobbie=input("input your data :->").split(",")
user={}
user['name']=name
user['age']=age
user['fav_movie']=fav_movie
user[fav_songs]=fav_songs
user['hobbie']=hobbie
for i,j in user.items():
    print(f"{i}:{j}")
