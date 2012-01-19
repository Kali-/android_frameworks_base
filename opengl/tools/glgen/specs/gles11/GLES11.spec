void glBindBuffer ( GLenum target, GLuint buffer )
void glBufferData ( GLenum target, GLsizeiptr size, const GLvoid *data, GLenum usage )
void glBufferSubData ( GLenum target, GLintptr offset, GLsizeiptr size, const GLvoid *data )
void glClipPlanef ( GLenum plane, const GLfloat *equation )
void glClipPlanex ( GLenum plane, const GLfixed *equation )
void glColor4ub ( GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha )
void glColorPointer ( GLint size, GLenum type, GLsizei stride, GLint offset )
void glDeleteBuffers ( GLsizei n, const GLuint *buffers )
void glDrawElements ( GLenum mode, GLsizei count, GLenum type, GLint offset )
void glGenBuffers ( GLsizei n, GLuint *buffers )
void glGetBooleanv ( GLenum pname, GLboolean *params )
void glGetBufferParameteriv ( GLenum target, GLenum pname, GLint *params )
void glGetClipPlanef ( GLenum pname, GLfloat *eqn )
void glGetClipPlanex ( GLenum pname, GLfixed *eqn )
void glGetFixedv ( GLenum pname, GLfixed *params )
void glGetFloatv ( GLenum pname, GLfloat *params )
void glGetLightfv ( GLenum light, GLenum pname, GLfloat *params )
void glGetLightxv ( GLenum light, GLenum pname, GLfixed *params )
void glGetMaterialfv ( GLenum face, GLenum pname, GLfloat *params )
void glGetMaterialxv ( GLenum face, GLenum pname, GLfixed *params )
// void glGetPointerv ( GLenum pname, void **params )
void glGetTexEnvfv ( GLenum env, GLenum pname, GLfloat *params )
void glGetTexEnviv ( GLenum env, GLenum pname, GLint *params )
void glGetTexEnvxv ( GLenum env, GLenum pname, GLfixed *params )
void glGetTexParameterfv ( GLenum target, GLenum pname, GLfloat *params )
void glGetTexParameteriv ( GLenum target, GLenum pname, GLint *params )
void glGetTexParameterxv ( GLenum target, GLenum pname, GLfixed *params )
GLboolean glIsBuffer ( GLuint buffer )
GLboolean glIsEnabled ( GLenum cap )
GLboolean glIsTexture ( GLuint texture )
void glNormalPointer ( GLenum type, GLsizei stride, GLint offset )
void glPointParameterf ( GLenum pname, GLfloat param )
void glPointParameterfv ( GLenum pname, const GLfloat *params )
void glPointParameterx ( GLenum pname, GLfixed param )
void glPointParameterxv ( GLenum pname, const GLfixed *params )
void glPointSizePointerOES ( GLenum type, GLsizei stride, const GLvoid *pointer )
void glTexCoordPointer ( GLint size, GLenum type, GLsizei stride, GLint offset )
void glTexEnvi ( GLenum target, GLenum pname, GLint param )
void glTexEnviv ( GLenum target, GLenum pname, const GLint *params )
void glTexParameterfv ( GLenum target, GLenum pname, const GLfloat *params )
void glTexParameteri ( GLenum target, GLenum pname, GLint param )
void glTexParameteriv ( GLenum target, GLenum pname, const GLint *params )
void glTexParameterxv ( GLenum target, GLenum pname, const GLfixed *params )
void glVertexPointer ( GLint size, GLenum type, GLsizei stride, GLint offset )