const AWS = require('aws-sdk');

const lambda = new AWS.Lambda({region: 'us-east-2'});

return
params = {
  FunctionName: "flask-hello-world-dev-app",
  Name: "dev"
 };

lambda.getAlias(params, function(err, data) {
   if (err) console.log(err, err.stack); // an error occurred
   else     console.log(data);           // successful response
 });

