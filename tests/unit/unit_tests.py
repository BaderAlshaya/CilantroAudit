from test_answer import AnswerTests
from test_severity import SeverityTests
from test_response import ResponseTests
from test_question import QuestionTests
from test_audit_template import AuditTemplateTests
from test_audit_template_builder import AuditTemplateBuilderTests



if __name__ == '__main__':
    AnswerTests.run_tests()
    SeverityTests.run_tests()
    ResponseTests.run_tests()
    QuestionTests.run_tests()
    AuditTemplateTests.run_tests()
    AuditTemplateBuilderTests.run_tests()
