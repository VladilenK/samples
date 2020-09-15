using Microsoft.SharePoint.Client;
using Microsoft.SharePoint.Client.Application;
using OfficeDevPnP.Core;
using OfficeDevPnP.Core.Pages;
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
        static void Main(string[] args)
        {
            string siteUrl = "";

            AuthenticationManager am = new AuthenticationManager();
            using (var cc = am.GetWebLoginClientContext(siteUrl))
            {
                var page = cc.Web.AddClientSidePage();
                page.AddControl(new ClientSideText() { Text = "Hello PnP" });
                page.Save("testpage.pnp.01.aspx");

                var url = cc.Web.EnsureProperty(p => p.Url);
            }

        }
    }
}
