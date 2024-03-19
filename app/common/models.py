from django.db import models

# Create your models here.
class CommonModel(models.Model):
    # 생성된  시간 (고정)
    create_at = models.DateTimeField(auto_now_add=True)  

    # 데이터가 업데이트된 시간 (업데이트 할 때 마다 계속 시간이 변경)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # DB 에 테이블을 추가하지 마시오.
        abstract = True