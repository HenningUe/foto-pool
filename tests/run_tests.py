
from pathlib import Path
import pytest  # type: ignore


if __name__ == "__main__":
    FAIL_FAST = "-x"
    test_dir = Path(__file__).parent
    extra_args = []
    # extra_args = ['-k', 'test_billing_finish_for_pmt or test_billing_finish_for_xil']
    extra_args = ['-k', 'test_interactive_2fa_authentication']
    pytest.main([test_dir, FAIL_FAST] + extra_args)
