pipeline {
  agent any
  stages {
    stage('Build') {
        steps {
            sh 'echo "Building..."'
        }
    }

    stage('Test') {
        environment {
            SEMGREP_COMMIT = "${env.GIT_COMMIT}"
            SEMGREP_REPO_NAME = "andyrat33/semgrep_test"
            SEMGREP_REPO_URL = https://github.com/andyrat33/semgrep_test
        }
        steps {
            sh '''echo "Semgrep Testing..."
            echo "COMMIT ID ${GIT_COMMIT}"
            ls -la
            printenv
            docker run -v $(pwd):/src --workdir /src returntocorp/semgrep-agent:v1 python -m semgrep_agent --config s/andyrat33:unsafe-crypto

            '''
        }
       }
  }

}