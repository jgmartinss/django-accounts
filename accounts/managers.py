from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, nickname, password, **kwargs):

        email = self.normalize_email(email)
        is_superuser = kwargs.pop('is_superuser', False)

        user = self.model(
            email=email,
            nickname=nickname,
            is_active=True,
            is_superuser=is_superuser,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password, **kwargs):
        super_user = self.create_user(email=email, nickname=nickname, password=password)
        super_user.is_admin = True
        super_user.is_superuser = True
        super_user.is_active = True
        super_user.save(using=self._db)
        return super_user
