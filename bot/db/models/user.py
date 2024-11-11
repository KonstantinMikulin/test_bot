from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.db import Base
from bot.db.models.mixins import TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = 'users'
    
    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    
    weights: Mapped[list['Weight']] = relationship(back_populates='user') # type:ignore # noqa: F821
    measurements_waist: Mapped[list["MeasureWaist"]] = relationship(  # type:ignore # noqa: F821
        back_populates="user"
    )
    measurements_hips: Mapped[list["MeasureHips"]] = relationship(  # type:ignore # noqa: F821
        back_populates="user"
    )
    measurements_bicep: Mapped[list["MeasureBicep"]] = relationship(  # type:ignore # noqa: F821
        back_populates="user"
    )
