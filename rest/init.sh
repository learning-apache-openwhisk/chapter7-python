APIHOST=$(wsk property get | awk '/whisk API host/ { print $4}')      
APIVERSION=$(wsk property get | awk '/whisk API version/ { print $4}')    
AUTH=$(wsk property get | awk '/whisk auth/ { print $3 }')         
NAMESPACE=$(wsk property get | awk '/whisk namespace/ { print $3}')    
URL="https://$APIHOST/api/$APIVERSION/namespaces/$NAMESPACE"                     

