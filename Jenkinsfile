pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'pip3 install -r requirements.txt || pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'python3 -m flake8 src/ tests/ --max-line-length=88'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=80'
            }
        }

        stage('Security') {
            steps {
                sh 'pip3 install pip-audit || pip install pip-audit'
                sh 'python3 -m pip_audit -r requirements.txt'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline passed! Safe to deploy.'
        }
        failure {
            echo '❌ Pipeline failed! Check the logs above.'
        }
    }
}
