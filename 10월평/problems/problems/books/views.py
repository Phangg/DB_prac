from webbrowser import get
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    # GET으로 들어오는 경우, 쿼리셋을 반환한다.
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    # Q 2.
    # POST로 들어오는 경우 요청받은 데이터의 유효성 검증 진행
    # 통과 시, 저장 후 반환 + 201 상태코드
    # 통과 못하면, 400 상태코드 반환
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    # 3,4,5 번 문제에서 사용될 book 위에서 먼저 받기
    book = get_object_or_404(Book, pk=book_pk)
    
    # Q 3.
    # GET -> 데이터 반환
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    # Q 4.
    # DELETE -> 삭제, 삭제 메시지 반환
    elif request.method == 'DELETE':
        book.delete()
        delete_message = {
            'delete': f'{book_pk}',
        }
        return Response(delete_message)
    # Q 5.
    # PUT -> 수정할 대상과 요철 유효성 검증
    # 통과 시, 저장 후 반환
    # 통과 못하면, 400 상태코드 반환
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    # Q 7.
    # 쿼리셋 반환
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    # 댓글이 생성될 book, 요청 유효성 검증
    # 통과 시, 저장 후 반환 + 201 상태코드
    # 참조 게시글 직접 입력 방지
    # 통과 못하면, 400 상태코드 반환
    book = Book.objects.get(pk=book_pk)
    serializer = CommentSerializer(book, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(book=book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # 9,10번에서 사용될 comment 미리 받기
    comment = get_object_or_404(Comment, pk=comment_pk)
    # Q 9.
    # 인스턴스 반환
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # Q 10.
    # 삭제, 삭제 메세지 반환
    elif request.method == 'DELETE':
        comment.delete()
        delete_message = {
            'delete': f'{comment_pk}',
        }
        return Response(delete_message)
