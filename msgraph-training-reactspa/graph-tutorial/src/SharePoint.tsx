import React from "react";
// import React, { Component, MouseEvent } from "react";
import { Table } from "reactstrap";
import moment from "moment";
import { Site } from "microsoft-graph";
import { config } from "./Config";
import { getSites } from "./GraphService";
import withAuthProvider, { AuthComponentProps } from "./AuthProvider";

// export class Button extends Component {
//   handleClick(event: MouseEvent) {
//     event.preventDefault();
//     alert(event.currentTarget.tagName); // alerts BUTTON
//   }

//   render() {
//     return <button onClick={this.handleClick}>{this.props.children}</button>;
//   }
// }

interface SharepointState {
  sites: Site[];
  count: number;
}

// Helper function to format Graph date/time
function formatDateTime(dateTime: string | undefined) {
  if (dateTime !== undefined) {
    return moment.utc(dateTime).local().format("M/D/YY h:mm A");
  }
}

class Sharepoint extends React.Component<AuthComponentProps, SharepointState> {
  constructor(props: any) {
    super(props);
    this.state = {
      sites: [],
      count: 0,
    };
  }

  private handleClick = async (event: React.MouseEvent<HTMLButtonElement>) => {
    var accessToken = await this.props.getAccessToken(config.scopes);
    var searchFor = document.getElementById("searchfor") as HTMLInputElement;
    console.log("keyword:", searchFor.value);
    var sites = await getSites(accessToken, searchFor.value);
    console.log("cdm Sites:", sites);
    // Update the array of sites in state
    this.setState({ sites: sites.value });
    this.setState(({ count }) => ({
      count: count + 1,
    }));
  };

  async componentDidMount() {
    try {
      // Get the user's access token
      var accessToken = await this.props.getAccessToken(config.scopes);
      // Get the user's sites
      var sites = await getSites(accessToken, "*");
      console.log("cdm Sites:", sites);
      // Update the array of sites in state
      this.setState({ sites: sites.value });
    } catch (err) {
      this.props.setError("ERROR", JSON.stringify(err));
    }
  }

  // <renderSnippet>
  render() {
    return (
      <div>
        <h1>SharePoint Sites Lookup </h1>
        <React.Fragment>
          <span>Keyword:</span>
          <span>Count:{this.state.count}</span>
          <input type="search" name="keyword" id="searchfor"></input>
          <button onClick={this.handleClick}>Go Search</button>
          <br />
        </React.Fragment>
        <h2>SharePoint Sites found:</h2>
        <Table>
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Url</th>
              <th scope="col">Created</th>
              <th scope="col">Modified</th>
            </tr>
          </thead>
          <tbody>
            {this.state.sites.map(function (site: Site) {
              return (
                <tr key={site.id}>
                  <td>
                    <a href="some link">{site.displayName}</a>
                  </td>
                  <td>
                    <a href={site.webUrl}>{site.webUrl}</a>
                  </td>
                  <td>{formatDateTime(site.createdDateTime)}</td>
                  <td>{formatDateTime(site.lastModifiedDateTime)}</td>
                </tr>
              );
            })}
          </tbody>
        </Table>
      </div>
    );
  }

  // goClicked():
  //   | ((event: React.MouseEvent<HTMLButtonElement, MouseEvent>) => void)
  //   | undefined {
  //   console.log("Method under construction.");
  //   var accessToken = this.props.getAccessToken(config.scopes);
  //   console.log("aT:", accessToken);
  //   var sites = getSites(accessToken, "test");
  //   console.log("Sites:", sites);
  //   // Update the array of sites in state
  //   // this.setState({ sites: sites.value });
  //   return;
  // }
  // </renderSnippet>
}

export default withAuthProvider(Sharepoint);
