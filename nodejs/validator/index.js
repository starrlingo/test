const Joi = require('joi');

// required field: username, password, access_token
const schema = Joi.object().keys({
    username: Joi.string().alphanum().min(3).max(30).required(),
    password: Joi.string().regex(/^[a-zA-Z0-9]{3,30}$/).required(),
    birthyear: Joi.number().integer().min(1900).max(2013),
    email: Joi.string().email()
})

// normal case
var result = Joi.validate({ username: 'abc', password: 'pwd' }, schema);
if (result.error) {
    console.log('validation error:', result.error.message);
}

// wrong case1: missing required field
result = Joi.validate({ username: 'abc', birthyear: 1994 }, schema);
if (result.error) {
    console.log('validation error:', result.error.message);
}

// wrong case2: non-defined attribute were sent
result = Joi.validate({ username: 'abc', password: 'test', testing: true }, schema);
if (result.error) {
    console.log('validation error:', result.error.message);
}
