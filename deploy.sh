#Main
function main {

    if ask "Deploy to production?"; then
        echo "Deploying to production ... "

        #Push to Heroku production
        git push production master

        #Update database
        if ask "Update production database?"; then
            updateProductionDatabase
        fi
    fi

    if ask "Deploy to staging?"; then
        echo "Deploying to staging ... "

        #Push to Heroku staging
        git push staging master

        #Update database
        if ask "Update staging database?"; then
            updateStagingDatabase
        fi
    fi

    echo "Deploy complete!"
}

#Ask a yes or no question
function ask {
    while true; do
        # Ask the question
        read -p "$1 [y/n] " REPLY

        # No answer
        if [ -z "$REPLY" ]; then
            REPLY=N
        fi

        # Check if the reply is valid
        case "$REPLY" in
            Y*|y*) return 0 ;;
            N*|n*) return 1 ;;
        esac
    done
}

#Update database
function updateProductionDatabase()
{
    echo "Updating database ... "

    #Run syncdb
    heroku run python manage.py syncdb --remote production

    #Run migrate
    heroku run python manage.py migrate --remote production
}

#Update database
function updateStagingDatabase()
{
    echo "Updating database ... "

    #Run syncdb
    heroku run python manage.py syncdb --remote staging

    #Run migrate
    heroku run python manage.py migrate --remote staging
}

main
