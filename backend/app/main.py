import logging

from app.settings import DATABASE_URL
from app.shared.cache import Cache
from app.shared.db import Database
from app.shared.events import EventBus
from app.shared.http import App
from app.users import routes as users_routes
from app.users.repository import UserRepository
from app.users.service import UserService
from app.orders import routes as orders_routes
from app.orders.repository import OrderRepository
from app.orders.service import OrderService
from app.payments import routes as payments_routes
from app.payments.repository import PaymentRepository
from app.payments.service import PaymentService
from app.inventory import routes as inventory_routes
from app.inventory.repository import InventoryItemRepository
from app.inventory.service import InventoryItemService
from app.catalog import routes as catalog_routes
from app.catalog.repository import ProductRepository
from app.catalog.service import ProductService
from app.shipping import routes as shipping_routes
from app.shipping.repository import ShipmentRepository
from app.shipping.service import ShipmentService
from app.reviews import routes as reviews_routes
from app.reviews.repository import ReviewRepository
from app.reviews.service import ReviewService
from app.notifications import routes as notifications_routes
from app.notifications.repository import NotificationRepository
from app.notifications.service import NotificationService
from app.auth import routes as auth_routes
from app.auth.repository import SessionRepository
from app.auth.service import SessionService
from app.billing import routes as billing_routes
from app.billing.repository import InvoiceRepository
from app.billing.service import InvoiceService
from app.analytics import routes as analytics_routes
from app.analytics.repository import MetricRepository
from app.analytics.service import MetricService
from app.search import routes as search_routes
from app.search.repository import SearchQueryRepository
from app.search.service import SearchQueryService
from app.coupons import routes as coupons_routes
from app.coupons.repository import CouponRepository
from app.coupons.service import CouponService
from app.returns import routes as returns_routes
from app.returns.repository import ReturnRequestRepository
from app.returns.service import ReturnRequestService
from app.wishlist import routes as wishlist_routes
from app.wishlist.repository import WishlistItemRepository
from app.wishlist.service import WishlistItemService

logger = logging.getLogger(__name__)


def create_app() -> App:
    db = Database(DATABASE_URL)
    bus = EventBus()
    cache = Cache()
    app = App()
    users_routes.bind(UserService(UserRepository(db), bus, cache))
    app.include(users_routes.router)
    orders_routes.bind(OrderService(OrderRepository(db), bus, cache))
    app.include(orders_routes.router)
    payments_routes.bind(PaymentService(PaymentRepository(db), bus, cache))
    app.include(payments_routes.router)
    inventory_routes.bind(InventoryItemService(InventoryItemRepository(db), bus, cache))
    app.include(inventory_routes.router)
    catalog_routes.bind(ProductService(ProductRepository(db), bus, cache))
    app.include(catalog_routes.router)
    shipping_routes.bind(ShipmentService(ShipmentRepository(db), bus, cache))
    app.include(shipping_routes.router)
    reviews_routes.bind(ReviewService(ReviewRepository(db), bus, cache))
    app.include(reviews_routes.router)
    notifications_routes.bind(NotificationService(NotificationRepository(db), bus, cache))
    app.include(notifications_routes.router)
    auth_routes.bind(SessionService(SessionRepository(db), bus, cache))
    app.include(auth_routes.router)
    billing_routes.bind(InvoiceService(InvoiceRepository(db), bus, cache))
    app.include(billing_routes.router)
    analytics_routes.bind(MetricService(MetricRepository(db), bus, cache))
    app.include(analytics_routes.router)
    search_routes.bind(SearchQueryService(SearchQueryRepository(db), bus, cache))
    app.include(search_routes.router)
    coupons_routes.bind(CouponService(CouponRepository(db), bus, cache))
    app.include(coupons_routes.router)
    returns_routes.bind(ReturnRequestService(ReturnRequestRepository(db), bus, cache))
    app.include(returns_routes.router)
    wishlist_routes.bind(WishlistItemService(WishlistItemRepository(db), bus, cache))
    app.include(wishlist_routes.router)
    logger.info("registered %d routes", len(app.route_table()))
    return app
