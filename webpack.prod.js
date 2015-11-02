var path = require('path')
var webpack = require('webpack')
var jQuery = require('jQuery')
var HtmlWebpackPlugin = require('html-webpack-plugin')
var ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
  entry:
    [ 'bootstrap-webpack!./bootstrap.prod.js'
    , './index'
    ],
  output: {
    path: path.join(__dirname, '../gh-pages'),
    filename: 'static/stenodict-[hash:4].js',
    publicPath: '/'
  },
  plugins: [
    new HtmlWebpackPlugin(
      { template: './index.html'
      , inject: true
      , favicon: './favicon.png'
      }
    ),
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin(),
    new webpack.DefinePlugin({
      'process.env': {
        'NODE_ENV': '"production"'
      }
    }),
    new ExtractTextPlugin("static/style-[contenthash:4].css")
  ],
  module:
    { loaders:
      [ { test: /\.js$/
        , loaders: ['babel']
        , exclude: /node_modules/
        , include: __dirname
        }
      , { test: /bootstrap\/js\//
        , loader: 'imports?jQuery=jquery'
        }
      , { test: /\.woff.*|\.ttf|\.eot|\.svg$/
        , loader: "file?name=static/fnt-[hash:6].[ext]"
        }
      ]
    }
};
