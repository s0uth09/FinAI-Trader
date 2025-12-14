# Contributing to FinAI Trader

Thank you for considering contributing to FinAI Trader! We welcome contributions from the community to improve this AI-powered crypto trading assistant. Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

## Code of Conduct
Please note that this project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct.html). By participating, you are expected to uphold this code.

## How to Contribute
### Reporting Issues
- Use the [issue tracker](https://github.com/yourusername/fin-ai-trader/issues) to report bugs or suggest features.
- Check if the issue already exists before creating a new one.
- Use the provided templates for bug reports or feature requests.

### Pull Requests
1. Fork the repository and create a new branch for your changes: `git checkout -b feature/your-feature-name`.
2. Make your changes, ensuring they follow the coding style (use `pre-commit` hooks).
3. Write tests for new features or bug fixes.
4. Commit your changes with clear messages: `git commit -m "Add feature: your description"`.
5. Push to your fork: `git push origin feature/your-feature-name`.
6. Open a pull request against the `main` branch.
7. Ensure your PR passes all CI/CD checks.

### Development Setup
1. Clone the repo: `git clone https://github.com/yourusername/fin-ai-trader.git`.
2. Install dependencies: `make install`.
3. Set up environment: Copy `.env.example` to `.env` and fill in your keys (e.g., API keys for Binance, Stripe).
4. Run dev environment: `make dev`.
5. Run tests: `make test`.

### Style Guidelines
- Python code: Follow PEP 8, use Black for formatting.
- Commit messages: Use conventional commits (e.g., `feat:`, `fix:`, `docs:`).
- Documentation: Update `README.md` or `docs/` as needed.

### Areas for Contribution
- Improve AI models (e.g., add new strategies in `src/strategies/`).
- Enhance security (e.g., in `src/risk/`).
- Add new data sources (e.g., in `src/data/clients/`).
- Optimize CI/CD workflows.

If you have questions, open an issue or contact us at support@finai.com.

Happy contributing!
