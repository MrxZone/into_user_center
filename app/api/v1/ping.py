from app.core.ecode import ErrorCode
from app.routes.route import BaseRouter

router = BaseRouter(tags=["ping"])


@router.get("/", summary="服务测试")
async def ping():
    return ErrorCode.SUCCESS, {"msg": "pong"}
