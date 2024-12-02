from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
import jwt
from .serializer import *


url='https://graphql.anilist.co'

class Signup(APIView):
    def post(self, request):

        try:
            print('hi')
           
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'User created successfully'}, status=201)
            else:
                return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'message':'Error creating user'}, status=400)
        



class AniListSearch(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer = AniListSearchSerializer(data=request.data)
            if serializer.is_valid():
                search=data.get('search')
                genre=data.get('genre')
                if not search:
                    return Response({'message': 'The "search" field is required.'}, status=400)
                if search:
                    query='''
                                        query ($search: String!, $genre:String) {
                                        Page {
                                            media(search: $search,genre:$genre,type: ANIME) {
                                            id
                                            title {
                                                romaji
                                                english
                                                native
                                            }
                                            genres
                                            }
                                        }
                                        }'''
                    variables={
                        'search':search,
                        'genre':genre
                    }
                    response = requests.post(url, json={"query": query, "variables": variables})
                    if response.status_code==200:
                        data=response.json()
                        return Response(data, status=200)
                    else:
                        return Response({'message':'No Anime Found'}, status=400)
            else:
                return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'message':'Error searching anime'}, status=400)


class Prefrence(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
     
        try:
            serializer=PrefrenceSerializer(data=request.data)
            if serializer.is_valid():
                user=request.user
                prefrence=serializer.validated_data.get('prefrence')

                if prefrence:

                    is_pref=UserPrefrence.objects.filter(user=user)

                    if is_pref:
                        is_pref.delete()


                    user_prefrence=UserPrefrence.objects.create(
                        user=user,
                        prefrence=prefrence

                    )
                    user_prefrence.save()
                    return Response({'message':'Prefrence saved'}, status=200)
                
                else:
                    return Response({'message':'No prefrence provided'}, status=400)
            else:
                return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'message':'Error saving prefrence'}, status=400)
        

    
class Suggestion(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:

            user=request.user
            prefrence=UserPrefrence.objects.get(user=user)
          
            if prefrence:
                query='''
                              query ($genre: [String!]) {
                                Page {
                                    media(genre_in: $genre, type: ANIME) {
                                    id
                                    title {
                                        romaji
                                        english
                                        native
                                    }
                                    genres
                                    }
                                }
                                }
   
                                    '''
                variables={
                    'genre':prefrence.prefrence[0].split(',')
                }
        
        
                response = requests.post(url, json={"query": query, "variables": variables})
                if response.status_code==200:
                    return Response(response.json(), status=200)
            
                else:
                    return Response({'message':'Error fetching suggestion'}, status=400)
            else:
               
                return Response({'message':'No prefrence provided'}, status=400)
        except Exception as e:
            return Response({'message':'Error fetching suggestions'}, status=400)
      

               







                



            

        

        






        
       


        


