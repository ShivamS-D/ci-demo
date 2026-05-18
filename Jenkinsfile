pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                    apt-get update -q
                    apt-get install -y python3 python3-pip python3-venv -q
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    flake8 src/ tests/ --max-line-length=88
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=80
                '''
            }
        }

        stage('Security') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install pip-audit
                    pip-audit -r requirements.txt
                '''
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
