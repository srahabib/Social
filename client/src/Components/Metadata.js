import React from 'react'

function Metadata() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <h2 className="text-2xl font-semibold mb-4 text-blue-500">Metadata</h2>
      <div className="overflow-x-auto">
        <table className="table-auto w-full border-collapse border border-blue-300">
          <thead className="bg-blue-500">
            <tr>
              <th className="border border-gray-300 px-4 py-2 text-white">Column Name</th>
              <th className="border border-gray-300 px-4 py-2 text-white">Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td className="border border-gray-300 px-4 py-2">user_name</td>
              <td className="border border-gray-300 px-4 py-2">This variable contains the username of the user who tweeted the content.</td>
            </tr>
            <tr>
              <td className="border border-gray-300 px-4 py-2">date</td>
              <td className="border border-gray-300 px-4 py-2">This variable represents the date when the content was posted.</td>
            </tr>
            <tr>
              <td className="border border-gray-300 px-4 py-2">likes</td>
              <td className="border border-gray-300 px-4 py-2">This variable stores the number of likes that the content received.</td>
            </tr>
            <tr>
              <td className="border border-gray-300 px-4 py-2">retweets</td>
              <td className="border border-gray-300 px-4 py-2">This variable stores the number of retweets that the content received.</td>
            </tr>
            <tr>
              <td className="border border-gray-300 px-4 py-2">content</td>
              <td className="border border-gray-300 px-4 py-2">This variable contains the actual text content of the tweet.</td>
            </tr>
            <tr>
              <td className="border border-gray-300 px-4 py-2">hashtags</td>
              <td className="border border-gray-300 px-4 py-2">This variable contains any hashtags included in the content, if applicable.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default Metadata
