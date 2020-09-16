using Microsoft.Azure.ActiveDirectory.GraphClient;
using Microsoft.SharePoint.Client;
using Microsoft.SharePoint.Client.Application;
using OfficeDevPnP.Core;
using OfficeDevPnP.Core.Pages;
using OfficeDevPnP.Core.Sites;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security;
using System.Text;
using System.Threading.Tasks;

namespace myConsolePnPCoreOnline01
{
    class Program
    {
        public static string TenantUrl = "";
        public static string userName = "";
        public static string password = "";
        static async Task Main(string[] args)
        {
            SecureString secureString = new SecureString();
            password.ToList().ForEach(secureString.AppendChar);
            var credentials = new SharePointOnlineCredentials(userName, secureString);

            using (ClientContext context = new ClientContext(TenantUrl)){
                context.Credentials = credentials;

/*                CommunicationSiteCollectionCreationInformation communicationSiteInfo = new CommunicationSiteCollectionCreationInformation
                {
                    Title = "PnP Demo Communication Site 75",
                    Url = "",
                    //possible SiteDesign values can be CommunicationSiteDesign.Showcase, CommunicationSiteDesign.Blank,  
                    SiteDesign = CommunicationSiteDesign.Topic,
                    Description = "Demo Description",
                    Owner = userName
                    //Classification = "HR",  
                    //Lcid = 1033  
                };
                var createCommSite = await context.CreateSiteAsync(communicationSiteInfo);
*/
                TeamNoGroupSiteCollectionCreationInformation teamSiteInfo = new TeamNoGroupSiteCollectionCreationInformation
                {
                    Title = "PnP Demo no-group Tesam Site 83",
                    Url = "https://.sharepoint.com/sites/test83",
                    Description = "Demo Description",
                    Owner = userName
                };
                
                var createTeamSite = await context.CreateSiteAsync(teamSiteInfo);

                Task.WaitAll();

/*                var teamContext = await context.CreateSiteAsync(
                    new TeamSiteCollectionCreationInformation
                    {
                        Alias = "myPnPmodernTeamSite76", // Mandatory
                        DisplayName = "myPnPmodernTeamSite76", // Mandatory
                        Description = "description", // Optional
                        //Classification = "classification", // Optional
                        //IsPublic = true, // Optional, default true
                    });
                teamContext.Load(teamContext.Web, w => w.Url);
                teamContext.ExecuteQueryRetry();
                Console.WriteLine(teamContext.Web.Url);
*/

            }
        }
    }
}
