import re

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms import \
    StringField, PasswordField, TextAreaField, \
    HiddenField, FloatField, IntegerField, DecimalField, RadioField, SelectField, \
    SelectMultipleField, BooleanField, DateField, DateTimeField, MultipleFileField, \
    SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, ValidationError


def phone_required(form, field):
    print(field.data)
    username = field.data
    pattern = r'^1[0-9]{10}$'
    if not re.search(pattern, username):
        raise ValidationError('请输入手机号码')
    return field


class LoginFormNew(FlaskForm):
    username = StringField(label='用户名') # default validators widget description
    password = PasswordField(label='密码')
    submit = SubmitField(label='登录')


class UserForm(FlaskForm):
    # def __init__(self, csrf_enabled, *args, **kwargs):
    #     super().__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

    username = StringField(label='用户名', validators=[phone_required])  # default validators widget description
    password = PasswordField(label='密码')
    birth_date = DateField(label='生日', validators=[DataRequired('请输入生日')])
    age = IntegerField(label='年龄')
    submit = SubmitField(label='新增')

    # def validate_username(self, field):
    #     print(field.data)
    #     username = field.data
    #     pattern = r'^1[0-9]{10}$'
    #     if not re.search(pattern, username):
    #         raise ValidationError('请输入手机号码')
    #     return field


class UserAvatarForm(FlaskForm):
    avatar = FileField(label='头像', validators=[
        FileRequired('请选择图片文件'),
        FileAllowed('jpg, png', '仅支持jpg,png')
    ])


class ProductEditForm(FlaskForm):
    name = StringField(label='商品标题', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    }, description='商品标题不超过200字')
    content = TextAreaField(label='商品描述', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    desc = StringField(label='商品推荐', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    types = SelectField(label='商品类型',
        choices=(('11', '实物商品'), ('12', '虚拟商品')),
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入'
    })
    price = IntegerField(label='销售价格', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    origin_price = FloatField(label='商品原价', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    img = FileField(label='商品主图', render_kw={
        'class': '',
        'placeholder': ''
    })
    channel = StringField(label='渠道', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    buy_link = StringField(label='购买链接', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    status = SelectField(label='商品状态',
        choices=(('11', '销售中'), ('12', '已销售'), ('12', '未开始')),
        render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    sku_count = IntegerField(label='库存', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    remain_count = IntegerField(label='剩余库存', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    view_count = IntegerField(label='浏览次数', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    score = IntegerField(label='评分', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    is_valid = BooleanField(label='是否删除')
    reorder = IntegerField(label='商品排序', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })


class LoginForm(FlaskForm):
    username = StringField(label='用户名', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })
    password = PasswordField(label='密码', render_kw={
        'class': 'form-control',
        'placeholder': '请输入'
    })

    def validate_username(self, field):
        username = field.data
        return username