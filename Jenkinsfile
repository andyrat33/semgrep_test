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
            SEMGREP_REPO_URL = "${env.GIT_URL}"
            SEMGREP_JOB_URL = "${env.JOB_DISPLAY_URL}"
            SEMGREP_APP_TOKEN = credentials('SEMGREP_APP_TOKEN')
            SEMGREP_BRANCH = "${env.BRANCH_NAME}"
            BASELINE_REF = "${env.GIT_PREVIOUS_COMMIT}"
            SEMGREP_PR_ID = "123"
            SEMGREP_PR_TITLE = "Test"
        }
        steps {
            sh '''echo "Semgrep Testing..."
            echo "COMMIT ID ${GIT_COMMIT}"
            ls -la
            printenv
            docker run -v $(pwd):/src --workdir /src returntocorp/semgrep-agent:v1 \
            python -m semgrep_agent --config s/andyrat33:unsafe-crypto \
            --publish-deployment 63 \
            --publish-token $SEMGREP_APP_TOKEN \
            --baseline-ref $BASELINE_REF

            '''
        }
       }
  }

}