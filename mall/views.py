from flask import Blueprint, render_template, url_for, request, abort, flash, redirect

from forms import ProductEditForm
from models import Product, db

mall = Blueprint('mall', __name__, template_folder='templates', static_folder='static')

@mall.route('/product/list/<int:page>')
# @login_required
def product_list(page):
    page_size = 5
    name = request.args.get('name', '')
    product = Product.query.filter(Product.name.contains(name), Product.is_valid==True)
    page_data = product.paginate(page=page, per_page=page_size)
    return render_template('product_list.html', page_data=page_data, page_size=page_size)


@mall.route('/product/detail/<uid>')
def product_detail(uid):
    prod_obj = Product.query.filter_by(uid=uid).first_or_404()
    return render_template('product_detail.html', prod_obj=prod_obj)


@mall.route('/product/edit/<uid>', methods=['GET', 'POST'])
def product_edit(uid):
    prod_obj = Product.query.filter_by(uid=uid, is_valid=True).first()
    if prod_obj is None:
        abort(404)
    form = ProductEditForm(obj=prod_obj)
    if form.validate_on_submit():
        prod_obj.name = form.name.data
        prod_obj.content = form.content.data
        prod_obj.desc = form.desc.data
        prod_obj.types = form.types.data
        prod_obj.price = form.price.data
        prod_obj.origin_price = form.origin_price.data
        prod_obj.img = 'xxx.jpg'
        prod_obj.channel = form.channel.data
        prod_obj.buy_link = form.buy_link.data
        prod_obj.status = form.status.data
        prod_obj.sku_count = form.sku_count.data
        prod_obj.remain_count = form.remain_count.data
        prod_obj.view_count = form.view_count.data
        prod_obj.score = form.score.data
        prod_obj.is_valid = form.is_valid.data
        prod_obj.reorder = form.reorder.data
        db.session.add(prod_obj)
        db.session.commit()
        flash('修改商品成功', 'success')
        return redirect(url_for('mall.product_list', page=1))
    else:
        print(form.errors)
        flash('请修改页面中的页面错误', 'warning')
    return render_template('product_edit.html', form=form, uid=uid)


@mall.route('/product/add', methods=['GET', 'POST'])
def product_add():
    form = ProductEditForm()
    if form.validate_on_submit():
        prod_obj = Product(
            name=form.name.data,
            content=form.content.data,
            desc=form.desc.data,
            types=form.types.data,
            price=form.price.data,
            origin_price=form.origin_price.data,
            img='xxx.jpg',
            channel=form.channel.data,
            buy_link=form.buy_link.data,
            status=form.status.data,
            sku_count=form.sku_count.data,
            remain_count=form.remain_count.data,
            view_count=form.view_count.data,
            score=form.score.data,
            is_valid=form.is_valid.data,
            reorder=form.reorder.data,
        )
        db.session.add(prod_obj)
        db.session.commit()
        flash('新增商品成功', 'success')
        return redirect(url_for('mall.product_list', page=1))
    else:
        print(form.errors)
        flash('请修改页面中的页面错误', 'warning')
    return render_template('product_add.html', form=form)


@mall.route('/product/delete/<uid>', methods=['GET', 'POST'])
def product_delete(uid):
    prod_obj = Product.query.filter_by(uid=uid, is_valid=True).first()
    if prod_obj is None:
        return 'no'
    prod_obj.is_valid = False
    db.session.add(prod_obj)
    db.session.commit()
    return 'ok'
