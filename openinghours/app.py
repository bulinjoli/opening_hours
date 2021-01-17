from flask import Flask, request, abort
from flask_restplus import Resource, Api
import datetime

app = Flask(__name__)
api = Api(app)

@api.route('/opening_hours')
class OpeningHours(Resource):
    def post(self):
        result = ""
        data = request.get_json()#list = [time["type"] for time in data.items()]

        if data:
            # It wouldn't make much sense to have open after open value, so to have proper json we are creating
            # simple validation that would check if json is properly written, so we have open and close times all the time
            type_list = [time["type"] for key in data for time in data[key]] # creating a list of only types
            validation_list = [type_list[i] == type_list[i-1] for i in range(len(type_list))]  # list comprehension that is checking in case values are repeating one after another and returns True in that case
            if True in validation_list:
                abort(400, "Please check your json values, looks like you have types repeating one after another")

            # Transforming list so I can do validation for times
            converted_list = [(key, time["type"], time["value"]) for key in data for time in data[key]]
            validation_time_list = [(converted_list[i - 1][2] >= converted_list[i][2]) for i in range(len(converted_list)) if
                         converted_list[i][0] == converted_list[i - 1][0]]
            # Checking if there are wrong time values
            if True in validation_time_list:
                abort(400, "Please check your json values, looks like you wrong hours")

            # main method for creating string, could have been done also in comprehension list but looked too complex to be one liner in my opinion
            for key in data:
                times = data[key]
                if times:
                    time_string = ""
                    time_len = len(times) - 1
                    for time in times:
                        readable_time = datetime.datetime.fromtimestamp(
                            time["value"]
                        ).strftime('%I:%M %p')

                        # in case there is a day starting with close type time, that means that this closing time belongs to previous day
                        if time == times[0] and times[0]["type"] == "close":
                            result += str(readable_time)  # so we are adding value to previous string, before we add a new day to this string
                        else:
                            if time["type"] == "open":
                                time_string += str(readable_time) + " - "
                            else:
                                if time != times[time_len]:  # in case close time is not last, that means that we have another opening hours right after, so we add comma
                                    time_string += str(readable_time)+", "
                                else:
                                    time_string += str(readable_time)

                else:
                    time_string = "Closed"

                result += key if key == "monday" else ' \n'+key
                result += ": "+time_string

            print(result)

            return result
        else:
            abort(400, "Please add json of opening hours")

if __name__ == '__main__':
    app.run(debug=True)