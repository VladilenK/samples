
Auth:
            var credentials = new SharePointOnlineCredentials(userName, secureString);
            using (ClientContext context = new ClientContext(TenantUrl)){
                context.Credentials = credentials;


Can create 3 types of sites
- no-group Team site
- o365 group-based Team site
- Communication site





