pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '--user root'
        }
    }

    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 src/ tests/ --max-line-length=88'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=80'
            }
        }

        stage('Security') {
            steps {
                sh 'pip install pip-audit'
                sh 'pip-audit -r requirements.txt'
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
