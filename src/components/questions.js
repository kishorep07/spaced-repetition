import React from 'react';
import Table from './table';

export default class ProblemTable extends React.Component {

  state = {
    loading: true,
    data: null
  };

  async componentDidMount() {
    const url = "https://aov24ycxzl.execute-api.ap-south-1.amazonaws.com/default/lc-tracker";
    const response = await fetch(url);
    const json = await response.json();
    this.setState({ data: json, loading: false });
  }

  render() {
    if(this.state.loading) return <h1>Loading</h1>;
    return (
      <div>
      <h1>{this.state.data[0]['08/22/20'].date}</h1>
      <Table data = {this.state.data} />
      </div>
    );
  }
}
