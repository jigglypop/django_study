from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Music,Artist,Review
from .serializers import MusicSerializers,ArtistSerializers,ArtistDetailSerializers,ReviewSerializer
# Create your views here.

@api_view(['GET'])
# HTTP method의 GET요청
def index(request):
    '''
    음악 목록 정보

    '''
    music = Music.objects.all()
    serializer = MusicSerializers(music,many=True)
    # 쿼리셋이기 때문
    return Response(serializer.data)

@api_view(['GET'])
def detail(request,music_pk):
    '''
    음악 상세 정보

    '''
    music = get_object_or_404(Music,pk=music_pk)
    serializer = MusicSerializers(music)
    return Response(serializer.data)

# 아티스트 목록

@api_view(['GET'])
# HTTP method의 GET요청
def name(request):
    '''
    아티스트 목록 정보

    '''
    artists = Artist.objects.all()
    serializer = ArtistSerializers(artists,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profile(request,artist_pk):
    '''
    아티스트 상세 정보

    '''
    artist = get_object_or_404(Artist,pk=artist_pk)
    serializer = ArtistDetailSerializers(artist)
    return Response(serializer.data)


# 리뷰 작성

@api_view(['POST'])
def review_create(request,music_pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    return Response({'message':'review가 등록되었습니다.'})

@api_view(['PUT','DELETE'])
def review_update_delete(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data,instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'review가 수정되었습니다.'})
    else:
        review.delete()
        return Response({'message':'review가 삭제되었습니다.'})

