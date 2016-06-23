module Greenwich
  #===========================================================================
  # Module for matrixes
  #===========================================================================
  module Matrix
    module_function

    #-------------------------------------------------------------------------
    # Initialize an r-matrix to the identity matrix.
    #
    # @param:  <none>
    # @return: r  (Rotated matrix)
    #-------------------------------------------------------------------------
    def init_r
      return [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
      ]
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Rotate an r-matrix about the x-axis.
    #
    #   (  1        0            0      )
    #   (                               )
    #   (  0   + cos(phi)   + sin(phi)  )
    #   (                               )
    #   (  0   - sin(phi)   + cos(phi)  )
    #
    # @param:  r    (Rotation matrix)
    # @param:  phi  (Angle)
    # @return: r    (Rotated matrix)
    #-------------------------------------------------------------------------
    def rotate_x(r, phi)
      s = Math.sin(phi)
      c = Math.cos(phi)
      r[1][0] =   c * r[1][0] + s * r[2][0]
      r[1][1] =   c * r[1][1] + s * r[2][1]
      r[1][2] =   c * r[1][2] + s * r[2][2]
      r[2][0] = - s * r[1][0] + c * r[2][0]
      r[2][1] = - s * r[1][1] + c * r[2][1]
      r[2][2] = - s * r[1][2] + c * r[2][2]
      return r
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Rotate an r-matrix about the y-axis.
    #
    #   (  + cos(theta)     0      - sin(theta)  )
    #   (                                        )
    #   (       0           1           0        )
    #   (                                        )
    #   (  + sin(theta)     0      + cos(theta)  )
    #
    # @param:  r      (Rotation matrix)
    # @param:  theta  (Angle)
    # @return: r      (Rotated matrix)
    #-------------------------------------------------------------------------
    def rotate_y(r, theta)
      s = Math.sin(theta)
      c = Math.cos(theta)
      r[0][0] = c * r[0][0] - s * r[2][0]
      r[0][1] = c * r[0][1] - s * r[2][1]
      r[0][2] = c * r[0][2] - s * r[2][2]
      r[2][0] = s * r[0][0] + c * r[2][0]
      r[2][1] = s * r[0][1] + c * r[2][1]
      r[2][2] = s * r[0][2] + c * r[2][2]
      return r
    rescue => e
      raise
    end

    #-------------------------------------------------------------------------
    # Rotate an r-matrix about the z-axis.
    #
    #   (  + cos(psi)   + sin(psi)     0  )
    #   (                                 )
    #   (  - sin(psi)   + cos(psi)     0  )
    #   (                                 )
    #   (       0            0         1  )
    #
    # @param:  r    (Rotation matrix)
    # @param:  psi  (Angle)
    # @return: r    (Rotated matrix)
    #-------------------------------------------------------------------------
    def rotate_z(r, psi)
      s = Math.sin(psi)
      c = Math.cos(psi)
      r[0][0] =   c * r[0][0] + s * r[1][0]
      r[0][1] =   c * r[0][1] + s * r[1][1]
      r[0][2] =   c * r[0][2] + s * r[1][2]
      r[1][0] = - s * r[0][0] + c * r[1][0]
      r[1][1] = - s * r[0][1] + c * r[1][1]
      r[1][2] = - s * r[0][2] + c * r[1][2]
      return r
    rescue => e
      raise
    end
  end
end

