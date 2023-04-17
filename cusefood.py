from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    html_content = '''
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    body {
                        font-family: gill sans,sans-serif;
                        font-size: 25px;
                        text-align: center;
                        background-color: #fffae6;
                        padding: 0;
                        margin: 0;
                    }
                    paragraph {
                        font-size: 20px;
                    }
                    button {
                        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                        font-size: 24px;
                        background-color: #FFA500;
                        color: #FFFFFF;
                        font-weight: bold;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        transition: all 0.3s ease;
                        box-shadow: 0 2px 2px rgba(0,0,0,0.3);
                    }
                    button:hover {
                        background-color: #FF8C00;
                    }
                        #pullout {
                        position: fixed;
                        top: 0;
                        right: 0;
                        width: 100px;
                        height: 100%;
                        background-color: #333;
                        color: #fff;
                        text-align: center;
                        line-height: 50px;
                        cursor: pointer;
                        transition: width 0.5s;
                        display: flex;
                        flex-direction: column;
                    }
                    #pullout:hover {
                        width: 200px;
                    }
                    #pullout span {
                        display: inline-block;
                        vertical-align: middle;
                        margin-left: 10px;
                        font-size: 24px;
                    }
                    #about-link {
                        color: #fff;
                        display: none;
                        font-size: 18px;
                    }
                    #pullout:hover #about-link {
                        display: inline-block;
                    }
                    .header-ribbon {
                        background-color: #002147;
                        color: #fff;
                        height: 50px;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        font-family: gill sans,sans-serif;
                        font-size: 40px;
                        font-weight: bold;
                        padding: 0;
                        margin: 0;
                        width: 100%;
                    }
                </style>
            </head>
            <body>
                <div class="header-ribbon">CuseCommunityEats</div>
                <div id="pullout">
                    <span>☰</span>
                    <a href="/AboutUs" id="about-link">About Us</a>
                    <a href="/FoodPantries" id="about-link">Food Pantries</a>
                    <a href="/GroceryStores" id="about-link">Grocery Stores</a>
                    <a href="/CommunityGardens" id="about-link">Community Gardens</a>
                </div>
                <h1>Food Resources in Syracuse</h1>
                <p>Access food pantries, soup kitchens, and grocery stores near you!</p>
                <button onclick="window.location.href='/MapDatabase'">Find Resources Near You</button>
                <p>Find nutritional advice for every life stage!</p>
                <button onclick="window.location.href='https://www.myplate.gov/life-stages'">Go to MyPlate.gov</button>
            </body>
        </html>
    '''
    return html_content


@app.route("/MapDatabase")
def Map_Database():
    html_content = '''
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    body {
                        font-family: gill sans,sans-serif;
                        font-size: 30px;
                        text-align: center;
                        background-color: #fffae6;
                    }
                </style>
            </head>
            <body>
                <h1>Food Resources in Syracuse</h1>
            </body>
        </html>
    '''
    return html_content

@app.route("/AboutUs")
def about():
    html_content = '''
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    body {
                        font-family: gill sans,sans-serif;
                        font-size: 30px;
                        text-align: center;
                        background-color: #fffae6;
                        padding-left: 60px;
                        padding-right: 60px;
                    }
                    p {
                        font-size: 24px;
                        text-align: justify;
                        text-indent: 50px;
                        text-align-last: justify;
                        margin-bottom: 20px;
                    }
                    ul {
                        list-style-type: none;
                        margin: 0;
                        padding: 0;
                    }
                    li {
                        font-size: 24px;
                        margin-bottom: 10px;
                        color: 000;
                    }
                    a {
                        color: #002147;
                        text-decoration: none;
                    }
                    a:hover {
                        text-decoration: underline;
                    }
                    footer {
                        font-size: 12px;
                        text-align: center;
                        margin-top: 50px;
                        color: #a6a6a6;
                    }
                </style>
            </head>
            <body>
                <h1>About Us</h1>
                <p>This project, headed by Allen Soberanes, Isabella Rosales, and Cindy Mendoza, was created as an entry to the CuseHacks Beta 2023 Hackathon. CuseCommunityEats aims to connect Syracuse, NY residents with various food resources in order to combat the difficulties of living in a food desert. We wanted to provide a multitude of resources from grocery stores, to food pantries, and even community gardens to make this website accessible to a wide range of income levels and family types. As students of SU, we have found it extremely difficult to navigate buying groceries in a food desert, especially with no car. For this reason, any location chosen on our interactive map can be linked to Google Maps, where the user can receive accurate walking, driving, or driving directions. We hope that this website decreases food insecurity issues in Syracuse and increases community knowledge of local food resources.</p>
                <h2>Connect with us!</h2>
                <ul>
                    <li><a href="https://www.linkedin.com/in/allensoberanes/" target="_blank">Allen Soberanes</a></li>
                    <li><a href="https://www.linkedin.com/in/isabella-rosales/" target="_blank">Isabella Rosales</a></li>
                    <li><a href="https://www.linkedin.com/in/cindy-mendoza-6668b41a3/" target="_blank">Cindy Mendoza</a></li>
                </ul>
                <footer>Made with Flask, Mu Editor, SQL, and Neovim</footer>
            </body>
        </html>
    '''
    return html_content

@app.route("/FoodPantries")
def Pantries_List():
    html_content = '''
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    body {
                        font-family: gill sans,sans-serif;
                        font-size: 15px;
                        background-color: #fffae6;
                        padding: 0;
                        margin: 0;
                    }
                    h2 {
                        margin-bottom: 5px;
                    }
                    p {
                        margin-top: 5px;
                        margin-bottom: 5px;
                    }
                    th,
                    td {
                        padding: 10px;
                    }
                </style>
                <title>Food Pantry List</title>
            </head>
            <body>
                <h1>Food Pantry List</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Address</th>
                            <th>Hours</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- ACRA Health Food Pantry -->
                        <tr>
                            <td>
                                <h2>ACR Health Food Pantry</h2>
                            </td>
                            <td>
                                <p>627 W. Genesee Street<br>Syracuse, NY 13204</p>
                            </td>
                            <td>
                                <p>M-F 8:30am-4:30pm</p>
                            </td>
                        </tr>
                        <!-- All Faiths Food Pantry -->
                        <tr>
                            <td>
                                <h2>All Faiths Food Pantry</h2>
                            </td>
                            <td>
                                <p>406 Court Street<br>Syracuse, NY 13208</p>
                            </td>
                            <td>
                                <p>T & W 11am-2:45pm</p>
                            </td>
                        </tr>
                        <!-- Assumption Church Pantry -->
                        <tr>
                            <td>
                                <h2>Assumption Church Pantry</h2>
                            </td>
                            <td>
                                <p>808 N Salina St<br>Syracuse, NY 13208</p>
                            </td>
                            <td>
                                <p>M-F 9:30am-12:30PM</p>
                            </td>
                        </tr>
                        <!-- Baldwinsville Community Food Pantry -->
                        <tr>
                            <td>
                                <h2>Baldwinsville Community Food Pantry</h2>
                            </td>
                            <td>
                                <p>17 W. Genesee St<br>Baldwinsville, NY 13027</p>
                            </td>
                            <td>
                                <p>M-F 10am-1pm</p>
                            </td>
                        </tr>
                        <!-- Basilica of Sacred Heart Food Pantry -->
                        <tr>
                            <td>
                                <h2>Basilica of Sacred Heart Food Pantry</h2>
                            </td>
                            <td>
                                <p>927 Park Ave.<br>Syracuse, NY 13204</p>
                            </td>
                            <td>
                                <p>T 4:30 - 6:30 pm<br>Closed week of holidays</p>
                            </td>
                        </tr>
                        <!-- Bayberry Food Pantry (United Church of Christ) -->
                        <tr>
                            <td>
                                <h2>Bayberry Food Pantry (United Church of Christ)</
				</td>
				<td>
					<p>215 Blackberry Rd<br>Liverpool, NY 13090</p>
				</td>
				<td>
					<p>Every 2nd T 3 - 5 pm</p>
				</td>
			</tr>
        </html>
    '''
    return html_content

@app.route("/GroceryStores")
def Grocery_List():
    html_content = '''
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                body {
                    font-family: gill sans,sans-serif;
                    font-size: 30px;
                    text-align: center;
                    background-color: #fffae6;
                }
                table {
                    margin: 0 auto;
                    font-family: arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                }
                td, th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }
                th {
                    background-color: #dddddd;
                }
            </style>
        </head>
        <body>
            <h1>Grocery Stores in Syracuse</h1>
            <table>
              <tbody>
                <tr>
                  <th>Name</th>
                  <th>Address</th>
                  <th>Hours of Operation</th>
                </tr>
                <tr>
                  <td>
                    <h2>Store 1</h2>
                  </td>
                  <td>
                    <p>123 Main St<br>Syracuse, NY 12345</p>
                  </td>
                  <td>
                    <p>Monday-Friday: 9am-5pm</p>
                  </td>
                </tr>
                <tr>
                  <td>
                    <h2>Store 2</h2>
                  </td>
                  <td>
                    <p>456 Elm St<br>Syracuse, NY 12345</p>
                  </td>
                  <td>
                    <p>Monday-Friday: 8am-6pm</p>
                  </td>
                </tr>
                <tr>
                  <td>
                    <h2>Store 3</h2>
                  </td>
                  <td>
                    <p>789 Oak St<br>Syracuse, NY 12345</p>
                  </td>
                  <td>
                    <p>Monday-Friday: 10am-8pm</p>
                  </td>
                </tr>
              </tbody>
            </table>
        </body>
    </html>
    '''

    return html_content



@app.route("/CommunityGardens")
def Gardens_List():
    html_content = '''
        <!DOCTYPE html>
        <html>
            <head>
                <style>
                    body {
                        font-family: gill sans,sans-serif;
                        font-size: 30px;
                        text-align: center;
                        background-color: #fffae6;
                    }
                </style>
            </head>
            <body>
                <h1>Community Gardens in Syracuse</h1>
            </body>
        </html>
    '''
    return html_content



