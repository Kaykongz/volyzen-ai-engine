Volyzen AI Trading Engine
The Volyzen AI Trading Engine is a production-ready, high-performance algorithmic trading microservice built with Python and FastAPI. It provides a robust foundation for backtesting, paper trading, and live execution across multiple exchanges with built-in risk management and compliance features.
Features
Multi-Exchange Connectivity: Modular adapters for Binance, OANDA, and DEXs like Uniswap.
	AI-Ready Strategies: A structured framework for defining and executing complex trading logic.
	Multiple Trading Modes: Seamlessly switch between Backtest, Paper, and Live trading.
	Integrated Risk Engine: ATR-based position sizing, drawdown breakers, and session controls.
	GDPR-Aligned Compliance: Endpoints for managing user consent and legal documentation.
	Real-time Updates: WebSocket support for live PnL, equity, and trade events.
	Containerized & Deployable: Ready for deployment with Docker and a Railway template.
Tech Stack
Framework: FastAPI
	Database: PostgreSQL with SQLAlchemy ORM and Alembic for migrations.
	Async: Uvicorn/Gunicorn, asyncio
	Data Analysis: Pandas, pandas-ta
	Scheduling: APScheduler
	Authentication: JWT (Bearer Tokens)
Getting Started
Prerequisites
Python 3.11+
Docker & Docker Compose
PostgreSQL database
1. Environment Variables
Create a .env file from the example and fill in the required values.
cp .env.example .env

Key Environment Variables:
	DATABASE_URL: Your PostgreSQL connection string.

SECRET_KEY: A secret key for JWT token generation.
ALGORITHM: The algorithm for JWT encoding (e.g., HS256).
ACCESS_TOKEN_EXPIRE_MINUTES: Token expiry time.
BINANCE_API_KEY, BINANCE_API_SECRET: Credentials for Binance.
OANDA_API_KEY, OANDA_ACCOUNT_ID: Credentials for OANDA.
2. Installation & Database Migration
# Install dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

3. Running the Service
Locally with Uvicorn
uvicorn app.main:app --reload

With Docker
docker-compose up --build

The API will be available at http://localhost:8000. The interactive documentation can be accessed at http://localhost:8000/docs.
API Contract & Manus.im Integration
The engine exposes a RESTful API for all operations. The full contract is defined in the OpenAPI 3.1 specification.
For integration with the Manus.im front-end, the application should use the generated TypeScript SDK (@volyzen/engine-client). The front-end must set the NEXT_PUBLIC_ENGINE_URL environment variable to point to the deployed URL of this microservice. The SDK will handle authentication and API calls seamlessly.
Makefile Targets for Acceptance Evidence
make test: Run all unit and integration tests.
make coverage: Generate a test coverage report.
make backtest-demo: Run a demo backtest for the ScriptStrategy and output results to reports/backtest_script_strategy.json.
make risk-audit-demo: Run a simulation that triggers risk management rules and outputs the audit trail to reports/risk_journal.csv.
