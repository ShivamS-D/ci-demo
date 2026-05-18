pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'pip3 install -r requirements.txt'
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
                sh 'pip3 install pip-audit'
                sh 'pip-audit -r requirements.txt'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ci-demo:latest .'
                sh 'docker run ci-demo:latest'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'All checks passed. Deploying to production...'
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
```
