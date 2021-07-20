from fbs_runtime.application_context.PyQt5 import ApplicationContext
from MainWin import MainWindowUI

import sys


if __name__ == '__main__':
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = MainWindowUI()
    window.setWindowTitle("Loan Workflow Admin v3.4.0")
    window.resize(1250, 800)
    window.show()
    exit_code = appctxt.app.exec()  # 2. Invoke run()
    sys.exit(exit_code)
