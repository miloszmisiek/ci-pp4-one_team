/**
 * @jest-environment jsdom
 */

const { TestScheduler } = require("jest");

/* jshint esversion: 8 */
/**
 * @jest-environment jsdom
 */

 beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("base.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
  });


  describe("sortTable contains correct variables", () => {
    test("table exists", () => {
        expect(table in sortTable).toBe(true);
    })
  })