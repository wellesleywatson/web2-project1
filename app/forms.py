
from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField, FileField
from wtforms.validators import Required, Email, optional

class ProfileForm(Form):
      first_name = TextField('First Name', validators=[Required()])
      last_name = TextField('Last Name', validators=[Required()])
      age = IntegerField('Age', validators=[Required()])
      sex = SelectField('Sex', choices=[('Male','Male'),('Female','Female')] , validators=[Required()])
      image  = FileField('Image', validators=[Required()])

