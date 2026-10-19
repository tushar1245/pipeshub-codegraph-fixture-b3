from app.reviews.models import Review


def test_review_archive():
    review = Review(product_id="p-1", rating="5")
    review.archive()
    assert not review.is_active()
