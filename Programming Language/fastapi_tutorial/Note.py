# # Pydantic
# from datetime import datetime
# from typing import List, Optional
# from pydantic import BaseModel


# class User(BaseModel):
#     id: int
#     name = 'John Doe'
#     signup_ts: Optional[datetime] = None
#     friends: List[int] = []


# external_data = {
#     'id': '123',
#     'signup_ts': '2019-06-01 12:22',
#     'friends': [1, 2, '3'],
# }
# user = User(**external_data)
# print(user.id)
# #> 123
# print(repr(user.signup_ts))
# #> datetime.datetime(2019, 6, 1, 12, 22)
# print(user.friends)
# #> [1, 2, 3]
# print(user.dict())
# """
# {
#     'id': 123,
#     'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
#     'friends': [1, 2, 3],
#     'name': 'John Doe',
# }
# """

# #=======================================================================
# # Request 
# from fastapi import FastAPI, Request

# app = FastAPI()


# @app.get("/users/{user_id:int}")
# def get_user(user_id: float, request: Request):
#     print(request.path_params)  # {'user_id': 123} 출력
#     return {"user_id": user_id}  # {"user_id": 123.0} 응답



# #=======================================================================
# # FastAPI는 위에서 아래로 진행하므로 다음을 유의

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/users/me")
# def get_current_user():
#     return {"user_id": 123}


# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}



# #=======================================================================
# # 쿼리 요청
# @app.get("/users")
# def get_users(is_admin: bool, limit: int = 100):  # 추가: q
#     return {"is_admin": is_admin, "limit": limit}  # 추가: q


# #=======================================================================
# #Enum 열거체
# from enum import Enum
# from fastapi import FastAPI

# app = FastAPI()

# class UserLevel(str,Enum):
#     b = "b"
#     c = "c"


# @app.get("/users")
# def get_users(grade: UserLevel = UserLevel.b):
#     return {"grade": grade}



# #=======================================================================
# # JSON 형식으로 POST요청
# from typing import Optional, List  # 추가: List

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl


# app = FastAPI()


# # 추가: Item 클래스
# class Item(BaseModel):
#     name: str
#     price: float
#     amount: int = 0


# class User(BaseModel):
#     name: str
#     password: str
#     avatar_url: Optional[HttpUrl] = None
#     inventory: List[Item] = []  # 추가: inventory


# @app.post("/users")
# def create_user(user: User):
#     return user


# # 추가: get_user()
# @app.get("/users/me")
# def get_user():
#     fake_user = User(
#         name="FastCampus",
#         password="1234",
#         inventory=[
#             Item(name="전설 무기", price=1_000_000),
#             Item(name="전설 방어구", price=900_000),
#         ]
#     )
#     return fake_user



# #=======================================================================
# # DRY한 class overriding, status 직접설정
# class User(BaseModel):
#     name: str
#     avatar_url: HttpUrl = "https://icotar.com/avatar/fastcampus.png?s=200"


# class CreateUser(User):
#     password: str


# @app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
# def create_user(user: CreateUser):
#     return user


# #=======================================================================
# # Item GET
# from typing import List

# from fastapi import FastAPI, Query, Path
# from pydantic import BaseModel, parse_obj_as

# app = FastAPI()

# inventory = (
#     {
#         "id": 1,
#         "user_id": 1,
#         "name": "레전드포션",
#         "price": 2500.0,
#         "amount": 100,
#     },
#     {
#         "id": 2,
#         "user_id": 1,
#         "name": "포션",
#         "price": 300.0,
#         "amount": 50,
#     },
# )


# class Item(BaseModel):
#     name: str
#     price: float
#     amount: int = 0
    
# """
# - `gt`, `ge`, `lt`, `le`: 숫자
# - `min_length`, `max_length`: `str`
# - `min_items`, `max_items`: 컬렉션(e.g. `List`, `Set`)

# 뿐만 아니라 `regex` 옵션으로 정규표현식 검증도 가능합니다."""

# @app.get("/users/{user_id}/inventory", response_model=List[Item])
# def get_item(
#     #ellpisis = 필수값, None = 필수아님, gt = greater than
#     user_id: int = Path(..., gt=0, title="사용자 id", description="DB의 user.id"), 
#     name: str = Query(None, min_length=1, max_length=2, title="아이템 이름"),
# ):
#     user_items = []
#     for item in inventory:
#         if item["user_id"] == user_id:
#             user_items.append(item)

#     response = []
#     for item in user_items:
#         if name is None:
#             response = user_items
#             break
#         if item["name"] == name:
#             response.append(item)

#     return response



# #=======================================================================
# # POST 요청 시 pydantic class가 아닌 Json을 본문으로 갖는 요청 -> Field
# from typing import List

# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()


# class Item(BaseModel):
#     name: str = Field(..., min_length=1, max_length=100, title="이름")
#     price: float = Field(None, ge=0)
#     amount: int = Field(
#         default=1,
#         gt=0,
#         le=100,
#         title="수량",
#         description="아이템 갯수. 1~100 개 까지 소지 가능",
#     )


# @app.post("/users/{user_id}/item")
# def create_item(item: Item):
#     return item



# #=======================================================================

