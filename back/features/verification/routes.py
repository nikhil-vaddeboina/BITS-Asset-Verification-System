from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user
from app import RESULTS
from back.models import Asset
from back.features.verification.service import record_verification
from back.features.access.permissions import permission_required

verification_bp = Blueprint("verification", __name__)

@verification_bp.route("/scan")
@permission_required("scan_verify")
def scan():
    return render_template("verification/scan.html")

@verification_bp.route("/verify/<asset_id>", methods=["GET", "POST"])
@permission_required("scan_verify")
def verify(asset_id):
    asset = Asset.query.filter_by(asset_id=asset_id).first_or_404()
    if request.method == "POST":
        result = request.form.get("result", "")
        remarks = request.form.get("remarks", "").strip()
        errors = []
        if result not in RESULTS: errors.append("Choose a valid verification result.")
        if len(remarks) > 500: errors.append("Remarks must be 500 characters or fewer.")
        if errors:
            for error in errors: flash(error, "error")
        else:
            record = record_verification(asset, result, remarks, current_user.username)
            flash("Verification recorded successfully.", "success")
            return render_template("verification/result.html", asset=asset, record=record)
    return render_template("verification/verify.html", asset=asset, results=RESULTS)

@verification_bp.route("/lookup/<asset_id>")
@permission_required("scan_verify")
def lookup(asset_id):
    asset = Asset.query.filter_by(asset_id=asset_id).first()
    if not asset: return jsonify({"error": "No asset matches this QR code."}), 404
    return jsonify({"asset_id": asset.asset_id, "name": asset.name, "category": asset.category, "serial_number": asset.serial_number, "department": asset.department, "location": asset.location, "assigned_to": asset.assigned_to, "status": asset.status, "url": url_for("verification.verify", asset_id=asset.asset_id)})
