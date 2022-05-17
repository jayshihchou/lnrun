function send_to_line(message) {
  UrlFetchApp.fetch('https://notify-api.line.me/api/notify', {
    'headers': {
      'Authorization': 'Bearer ' + 'your code here',
    },
    'method': 'post',
    'payload': {
      'message':message,
      }
    });
}

function doGet(e) {
  Logger.log(e);
  if (e.parameter) {
    let p = e.parameter;
    if (p.status) {
      send_to_line(p.status);
      return HtmlService.createHtmlOutput('yes');
    }
  }
  return HtmlService.createHtmlOutput('failed');
}
