const path = require('path');
const webpack = require('webpack');
module.exports = {
  context: path.resolve(__dirname, 'dash'),
  entry: {
    app: './static/app.jsx',
  },
  output: {
    path: path.resolve(__dirname, './static/dist'),
    filename: '[name].bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.jsx?/,
        exclude: /node_modules/,
        use: 'babel-loader'
      }
    ]
  }

};
