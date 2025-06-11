from .help import router as help_router
from .scan import router as scan_router
from .start import router as start_router

routers = [start_router, help_router, scan_router]
