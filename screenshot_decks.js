const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const filePath = 'file://' + path.resolve('dist/21-information-modelling.html');

  // Slide 5
  await page.goto(filePath + '#5');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'slide_05.png' });

  // Slide 7
  await page.goto(filePath + '#7');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'slide_07.png' });

  // Slide 11
  await page.goto(filePath + '#11');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'slide_11.png' });

  await browser.close();
})();
