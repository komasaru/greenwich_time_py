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
      a_00 =     r[0][0]
      a_01 = c * r[0][1] - s * r[0][2]
      a_02 = s * r[0][1] + c * r[0][2]
      a_10 =     r[1][0]
      a_11 = c * r[1][1] - s * r[1][2]
      a_12 = s * r[1][1] + c * r[1][2]
      a_20 =     r[2][0]
      a_21 = c * r[2][1] - s * r[2][2]
      a_22 = s * r[2][1] + c * r[2][2]
      return [
        [a_00, a_01, a_02],
        [a_10, a_11, a_12],
        [a_20, a_21, a_22]
      ]
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
      a_00 =   c * r[0][0] + s * r[0][2]
      a_01 =       r[0][1]
      a_02 = - s * r[0][0] + c * r[0][2]
      a_10 =   c * r[1][0] + s * r[1][2]
      a_11 =       r[1][1]
      a_12 = - s * r[1][0] + c * r[1][2]
      a_20 =   c * r[2][0] + s * r[2][2]
      a_21 =       r[2][1]
      a_22 = - s * r[2][0] + c * r[2][2]
      return [
        [a_00, a_01, a_02],
        [a_10, a_11, a_12],
        [a_20, a_21, a_22]
      ]
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
      a_00 =  c * r[0][0] - s * r[0][1]
      a_01 =  s * r[0][0] + c * r[0][1]
      a_02 =      r[0][2]
      a_10 =  c * r[1][0] - s * r[1][1]
      a_11 =  s * r[1][0] + c * r[1][1]
      a_12 =      r[1][2]
      a_20 =  c * r[2][0] - s * r[2][1]
      a_21 =  s * r[2][0] + c * r[2][1]
      a_22 =      r[2][2]
      return [
        [a_00, a_01, a_02],
        [a_10, a_11, a_12],
        [a_20, a_21, a_22]
      ]
    rescue => e
      raise
    end
  end
end

