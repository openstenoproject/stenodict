var webpack = require('webpack')
var config = require("./webpack.prod.js")
var HtmlWebpackPlugin = require('html-webpack-plugin')

config.devtool = 'cheap-module-eval-source-map'
config.entry =
    [ 'webpack-hot-middleware/client'
    , 'bootstrap-webpack!./bootstrap.config.js'
    , './index'
    ]
config.plugins = [
    config.plugins[0],
    new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin()
  ]
module.exports = config
