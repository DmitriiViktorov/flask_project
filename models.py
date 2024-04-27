from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    followers = relationship('Subscription',
                             foreign_keys='Subscription.following_id',
                             back_populates='following')
    followings = relationship('Subscription',
                              foreign_keys='Subscription.follower_id',
                              back_populates='follower')

    @property
    def formatted_data(self):
        user_data = self.to_dict()
        user_data['followers'] = [subscription.follower.to_dict() for subscription in self.followers]
        user_data['followings'] = [subscription.following.to_dict() for subscription in self.followings]
        return user_data

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Subscription(Base):
    __tablename__ = "subscription"
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    following_id = Column(Integer, ForeignKey('user.id'))
    follower = relationship('User', foreign_keys=[follower_id], back_populates='followers')
    following = relationship('User', foreign_keys=[following_id], back_populates='followings')


