from flask import Blueprint, render_template, request
from sqlalchemy import or_
from app import RESULTS
from back.models import Asset, Verification
from back.features.access.permissions import permission_required

history_bp = Blueprint("history", __name__)

@history_bp.route("/history")
@permission_required("view_history")
def index():
    query = Verification.query.join(Asset)
    q = request.args.get("q", "").strip()
    result = request.args.get("result", "")
    if q:
        term = f"%{q}%"
        query = query.filter(or_(Asset.asset_id.ilike(term), Asset.name.ilike(term), Verification.verified_by.ilike(term), Verification.remarks.ilike(term)))
    if result: query = query.filter(Verification.result == result)
    items = query.order_by(Verification.verified_at.desc()).paginate(page=request.args.get("page", 1, type=int), per_page=15, error_out=False)
    return render_template("history/index.html", records=items, q=q, selected_result=result, results=RESULTS)
