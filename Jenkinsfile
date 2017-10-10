pipeline {
  agent any
  environment {
    BUILD_VERSION = '$(python3 -c \'from version import VERSION; print(VERSION,end="")\')'
    DOCKER_REPOSITORY = 'trstringer/verpy'
  }
  stages {
    stage('Build') {
      steps {
        echo "building..."
        sh "docker build -t ${env.DOCKER_REPOSITORY}:${env.BUILD_VERSION} -t ${env.DOCKER_REPOSITORY}:latest ."
        echo "installing virtual environment"
        sh "python3 -m venv venv"
        sh ". venv/bin/activate"
        sh "printenv"
        sh "pip install -r requirements.txt"
      }
    }
    stage('Unit Tests') {
      steps {
        sh "pytest"
      }
    }
    stage('Integration Tests') {
      steps {
        sh "integration/runner.sh"
      }
    }
    stage('Deliver') {
      when {
        expression {
          currentBuild.result == null || currentBuild.result == 'SUCCESS'
        }
      }
      steps {
        echo "pushing image to container registry..."
        sh "docker push ${env.DOCKER_REPOSITORY}:${env.BUILD_VERSION}"
        sh "docker push ${env.DOCKER_REPOSITORY}:latest"
      }
    }
  }
  post {
    always {
      sh "docker image prune -f"
    }
    failure {
      mail bcc: '', body: 'verpy build failed', cc: '', from: '', replyTo: '', subject: '<verpy> Build failed', to: 'github@trstringer.com'
    }
  }
}
